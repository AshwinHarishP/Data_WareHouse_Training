-- 1. Use a new database called campusdb
use campusdb

/* Output
switched to db campusdb
*/
  
-- 2. Create a collection enrollments and insert 4 student documents. 
db.createCollection("enrollments")
db.enrollments.insertMany([ 
  { 
    name: "Ananya Verma", 
    studentId: 101, 
    courses: ["Python", "Java"], 
    address: { city: "Delhi", state: "Delhi" }, 
    feesPaid: true 
  },
 
  { 
    name: "Rohan Mehta", 
    studentId: 102, 
    courses: ["Python", "AI"], 
    address: { city: "Bangalore", state: "Karnataka" }, 
    feesPaid: false 
  }, 

  { 
    name: "Sneha Kapoor", 
    studentId: 103, 
    courses: [], 
    address: { city: "Hyderabad", state: "Telangana" }, 
    feesPaid: true 
  },
 
  { 
  name: "Imran Shaikh", 
  studentId: 104, 
  courses: ["Data Science", "Java"], 
  address: { city: "Delhi", state: "Delhi" }, 
  feesPaid: false 
  } 
])
  
/* Output
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('682d5d266e4ec8ef8ed31a16'),
    '1': ObjectId('682d5d266e4ec8ef8ed31a17'),
    '2': ObjectId('682d5d266e4ec8ef8ed31a18'),
    '3': ObjectId('682d5d266e4ec8ef8ed31a19')
  }
}
*/

-- 3.  Display all student records
db.enrollments.find()

/* Output
{
  _id: ObjectId('682d5d266e4ec8ef8ed31a16'),
  name: 'Ananya Verma',
  studentId: 101,
  courses: [
    'Python',
    'Java'
  ],
  address: {
    city: 'Delhi',
    state: 'Delhi'
  },
  feesPaid: true
}
{
  _id: ObjectId('682d5d266e4ec8ef8ed31a17'),
  name: 'Rohan Mehta',
  studentId: 102,
  courses: [
    'Python',
    'AI'
  ],
  address: {
    city: 'Bangalore',
    state: 'Karnataka'
  },
  feesPaid: false
}
{
  _id: ObjectId('682d5d266e4ec8ef8ed31a18'),
  name: 'Sneha Kapoor',
  studentId: 103,
  courses: [],
  address: {
    city: 'Hyderabad',
    state: 'Telangana'
  },
  feesPaid: true
}
{
  _id: ObjectId('682d5d266e4ec8ef8ed31a19'),
  name: 'Imran Shaikh',
  studentId: 104,
  courses: [
    'Data Science',
    'Java'
  ],
  address: {
    city: 'Delhi',
    state: 'Delhi'
  },
  feesPaid: false
}
*/

-- 4. Find all students enrolled in "Python"
db.enrollments.find({courses: "Python"})

/* Output
{
  _id: ObjectId('682d5d266e4ec8ef8ed31a16'),
  name: 'Ananya Verma',
  studentId: 101,
  courses: [
    'Python',
    'Java'
  ],
  address: {
    city: 'Delhi',
    state: 'Delhi'
  },
  feesPaid: true
}
{
  _id: ObjectId('682d5d266e4ec8ef8ed31a17'),
  name: 'Rohan Mehta',
  studentId: 102,
  courses: [
    'Python',
    'AI'
  ],
  address: {
    city: 'Bangalore',
    state: 'Karnataka'
  },
  feesPaid: false
}
*/

-- 5. Find students from Delhi who have not paid fees
db.enrollments.find(
  { 
    "address.city": "Delhi",
    feesPaid: false
  }
)

/* Output 
{
  _id: ObjectId('682d5d266e4ec8ef8ed31a19'),
  name: 'Imran Shaikh',
  studentId: 104,
  courses: [
    'Data Science',
    'Java'
  ],
  address: {
    city: 'Delhi',
    state: 'Delhi'
  },
  feesPaid: false
}
*/
  
-- 6.  Add a new course "AI Fundamentals" to a specific student's courses array
db.enrollments.updateOne(
  {name: "Ananya Verma"},
  {$addToSet: {courses: "AI Fundamentals"}}
)

/* Output 
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}
*/

--7. Update the city of a specific student to "Mumbai"
db.enrollments.updateOne(
  {name: "Sneha Kapoor"},
  {$set:{ "address.city": "Mumbai", "address.state": "Maharashtra" }}
)

/* Output 
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}
*/
  
--8.  Set feesPaid to true for all students from "Delhi"
db.enrollments.updateMany(
  { "address.city": "Delhi" },
  { $set: { feesPaid: true } }
)

/* Output
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 2,
  modifiedCount: 1,
  upsertedCount: 0
}
*/
  
--9. Remove "Java" course from any student who has it
db.enrollments.updateMany(
  {courses: "Java"},
  {$pull: {courses: "Java"}}
)

/* Output 
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 2,
  modifiedCount: 2,
  upsertedCount: 0
}
*/

--10. Delete all students who have no courses enrolled (i.e., courses: [])
db.enrollments.deleteMany(
  {courses: {$size: 0}}
)

/* Output 
{
  acknowledged: true,
  deletedCount: 1
}
*/
