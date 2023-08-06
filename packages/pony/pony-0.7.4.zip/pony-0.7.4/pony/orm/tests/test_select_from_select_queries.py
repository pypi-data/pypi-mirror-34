import unittest

from pony.orm import *
from pony.orm.tests.testutils import *

db = Database('sqlite', ':memory:')

class Group(db.Entity):
    number = PrimaryKey(int)
    major = Required(str)
    students = Set('Student')

class Student(db.Entity):
    first_name = Required(unicode)
    last_name = Required(unicode)
    age = Required(int)
    group = Required('Group')
    scholarship = Required(int, default=0)
    courses = Set('Course')

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

class Course(db.Entity):
    name = Required(unicode)
    semester = Required(int)
    credits = Required(int)
    PrimaryKey(name, semester)
    students = Set('Student')

db.generate_mapping(create_tables=True)

with db_session:
    g1 = Group(number=123, major='Computer Science')
    g2 = Group(number=456, major='Graphic Design')
    s1 = Student(id=1, first_name='John', last_name='Smith', age=20, group=g1, scholarship=0)
    s2 = Student(id=2, first_name='Alex', last_name='Green', age=24, group=g1, scholarship=100)
    s3 = Student(id=3, first_name='Mary', last_name='White', age=23, group=g1, scholarship=500)
    s4 = Student(id=4, first_name='John', last_name='Brown', age=20, group=g2, scholarship=400)
    s5 = Student(id=5, first_name='Bruce', last_name='Lee', age=22, group=g2, scholarship=300)
    c1 = Course(name='Math', semester=1, credits=10, students=[s1, s2, s4])
    c2 = Course(name='Computer Science', semester=1, credits=20, students=[s2, s3])
    c3 = Course(name='3D Modeling', semester=2, credits=15, students=[s3, s5])


class TestSelectFromSelect(unittest.TestCase):
    @db_session
    def test_1(self):  # basic select from another query
        q = select(s for s in Student if s.scholarship > 0)
        q2 = select(s for s in q if s.scholarship < 500)
        self.assertEqual(set(s.first_name for s in q2), {'Alex', 'John', 'Bruce'})
        self.assertEqual(db.last_sql.count('SELECT'), 1)  # single SELECT...FROM expression

    @db_session
    def test_2(self):  # different variable name in the second query
        q = select(s for s in Student if s.scholarship > 0)
        q2 = select(x for x in q if x.scholarship < 500)
        self.assertEqual(set(s.first_name for s in q2), {'Alex', 'John', 'Bruce'})
        self.assertEqual(db.last_sql.count('SELECT'), 1)

    @db_session
    def test_3(self):  # selecting single column instead of entity in the second query
        q = select(s for s in Student if s.scholarship > 0)
        q2 = select(x.first_name for x in q if x.scholarship < 500)
        self.assertEqual(set(q2), {'Alex', 'Bruce', 'John'})
        self.assertEqual(db.last_sql.count('SELECT'), 1)

    @db_session
    def test_4(self):  # selecting single column instead of entity in the first query
        q = select(s.first_name for s in Student if s.scholarship > 0)
        q2 = select(name for name in q if 'r' in name)
        self.assertEqual(set(q2), {'Bruce', 'Mary'})
        self.assertEqual(db.last_sql.count('SELECT'), 1)

    @db_session
    def test_5(self):  # selecting hybrid property in the second query
        q = select(s for s in Student if s.scholarship > 0)
        q2 = select(x.full_name for x in q if x.scholarship < 500)
        self.assertEqual(set(q2), {'Alex Green', 'Bruce Lee', 'John Brown'})
        self.assertEqual(db.last_sql.count('SELECT'), 1)

    @db_session
    def test_6(self):  # selecting hybrid property in the first query
        q = select(s.full_name for s in Student if s.scholarship < 500)
        q2 = select(x for x in q if x.startswith('J'))
        self.assertEqual(set(q2), {'John Smith', 'John Brown'})
        self.assertEqual(db.last_sql.count('SELECT'), 1)

    @db_session
    @raises_exception(ExprEvalError, "s.scholarship > 0 raises NameError: name 's' is not defined")
    def test_7(self):  # test access to original query var name from the new query
        q = select(s.first_name for s in Student if s.scholarship < 500)
        q2 = select(x for x in q if s.scholarship > 0)

    @db_session
    def test_8(self):  # test using external name which is equal to original query var name
        class Dummy(object):
            scholarship = 1
        s = Dummy()
        q = select(s.first_name for s in Student if s.scholarship < 500)
        q2 = select(x for x in q if s.scholarship > 0)
        self.assertEqual(set(q2), {'John', 'Alex', 'Bruce'})

    @db_session
    def test_9(self):  # test reusing variable name from the original query
        q = select(s for s in Student if s.scholarship > 0)
        q2 = select(x for x in q for s in Student if x.scholarship < s.scholarship)
        self.assertEqual(set(s.first_name for s in q2), {'Alex', 'John', 'Bruce'})
        self.assertEqual(db.last_sql.count('SELECT'), 1)

    @db_session
    def test_10(self):  # test .filter()
        q = select(s for s in Student if s.scholarship > 0)
        q2 = q.filter(lambda a: a.scholarship < 500)
        q3 = select(x for x in q2 if x.age > 20)
        q4 = q3.filter(lambda b: b.age < 24)
        self.assertEqual(set(s.first_name for s in q4), {'Bruce'})
        self.assertEqual(db.last_sql.count('SELECT'), 1)

    @db_session
    def test_11(self):  # test .where()
        q = select(s for s in Student if s.scholarship > 0)
        q2 = q.where(lambda s: s.scholarship < 500)
        q3 = select(x for x in q2 if x.age > 20)
        q4 = q3.where(lambda x: x.age < 24)  # the name should be accessible in previous generator
        self.assertEqual(set(s.first_name for s in q4), {'Bruce'})
        self.assertEqual(db.last_sql.count('SELECT'), 1)

    @db_session
    @raises_exception(TypeError, 'Lambda argument `s` does not correspond to any variable in original query')
    def test_12(self):  # test .where()
        q = select(s for s in Student if s.scholarship > 0)
        q2 = q.where(lambda s: s.scholarship < 500)
        q3 = select(x for x in q2 if x.age > 20)
        q4 = q3.where(lambda s: s.age < 24)

    @db_session
    def test_13(self):  # select several expressions from the first query
        q = select((s.full_name, s.age) for s in Student if s.scholarship > 0)
        q2 = select(name for name, age in q if age < 24 and 'e' in name)
        self.assertEqual(set(q2), {'Mary White', 'Bruce Lee'})
        self.assertEqual(db.last_sql.count('SELECT'), 1)

    @db_session
    def test_14(self):  # select from entity with composite key
        q = select(c for c in Course if c.semester == 1)
        q2 = select(x.name for x in q if x.name.startswith('M'))
        self.assertEqual(set(q2), {'Math'})
        self.assertEqual(db.last_sql.count('SELECT'), 1)

    @db_session
    def test_15(self):  # SELECT ... FROM (SELECT alias.* FROM ...
        q = left_join(s for g in Group for s in g.students if g.number == 123 and s.scholarship > 0)
        q2 = select(x.full_name for x in q if x.scholarship > 100)
        self.assertEqual(set(q2), {'Mary White'})
        self.assertEqual(db.last_sql.count('SELECT'), 2)
        self.assertEqual(db.last_sql.count('LEFT JOIN'), 1)
        self.assertTrue('*' in db.last_sql)

    @db_session
    def test_16(self):   # SELECT ... FROM (grouped-query)
        q = select(g for g in Group if count(g.students) > 2)
        q2 = select(x.number for x in q)

        self.assertEqual(set(q2), {123})
        self.assertEqual(db.last_sql.count('SELECT'), 2)
        self.assertEqual(db.last_sql.count('LEFT JOIN'), 1)
        self.assertEqual(db.last_sql.count('GROUP BY'), 1)
        self.assertEqual(db.last_sql.count('HAVING'), 1)
        self.assertTrue('WHERE' not in db.last_sql)

    @db_session
    def test_17(self):  # SELECT ... FROM (grouped-query), t1 WHERE ...
        q = select(g for g in Group if count(g.students) > 2)
        q2 = select(x.major for x in q)

        self.assertEqual(set(q2), {'Computer Science'})
        self.assertEqual(db.last_sql.count('SELECT'), 2)
        self.assertEqual(db.last_sql.count('LEFT JOIN'), 1)
        self.assertEqual(db.last_sql.count('GROUP BY'), 1)
        self.assertEqual(db.last_sql.count('HAVING'), 1)

    @db_session
    def test_18(self):  # SELECT ... FROM (grouped-query returns composite keys), t1 WHERE ...
        q = select((c, count(c.students)) for c in Course if c.semester == 1 and count(c.students) > 1)
        q2 = select((x.name, x.credits, y) for x, y in q if x.credits > 10 and y < 3)

        self.assertEqual(set(q2), {('Computer Science', 20, 2)})
        self.assertEqual(db.last_sql.count('SELECT'), 2)
        self.assertEqual(db.last_sql.count('LEFT JOIN'), 1)
        self.assertEqual(db.last_sql.count('GROUP BY'), 1)
        self.assertEqual(db.last_sql.count('HAVING'), 1)
        self.assertEqual(db.last_sql.count('WHERE'), 2)

    @db_session
    def test_19(self):  # multiple for loops in the inner query
        q = select((g, s.first_name.lower()) for g in Group for s in g.students)
        q2 = select((g.major, n) for g, n in q if g.number == 123 and n[0] == 'j')
        self.assertEqual(set(q2), {('Computer Science', 'john')})

    @db_session
    def test_20(self):  # additional for loop with inlined subquery
        q = select((g, x.first_name.upper())
                   for g in Group
                   for x in select(s for s in Student if s.age < 22)
                   if x.group == g and g.number == 123 and x.first_name[0] == 'J')
        q2 = select(name for g, name in q if g.number == 123)
        self.assertEqual(set(q2), {'JOHN'})

    @db_session
    def test_21(self):
        objects = select(s for s in Student if s.scholarship > 200)[:]  # not query, but query result
        q = select(s.first_name for s in Student if s not in objects)
        self.assertEqual(set(q), {'John', 'Alex'})

    @db_session
    @raises_exception(TypeError, 'Query can only iterate over entity or another query (not a list of objects)')
    def test_22(self):
        objects = select(s for s in Student if s.scholarship > 200)[:]  # not query, but query result
        q = select(s.first_name for s in objects)


if __name__ == '__main__':
    unittest.main()
