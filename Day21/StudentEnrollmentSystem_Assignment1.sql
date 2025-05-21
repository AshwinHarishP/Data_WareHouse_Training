-- 1. Use a new database called campusdb
use campusdb

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
]

-- 3.  Display all student records
db.enrollments.find()

-- 4. Find all students enrolled in "Python"
db.enrollments.find({courses: "Python"})

-- 5. Find students from Delhi who have not paid fees
db.enrollments.find(
  { 
    "address.city": "Delhi",
    feesPaid: false
  }
)

-- 6.  Add a new course "AI Fundamentals" to a specific student's courses array
db.enrollments.updateOne(
  {name: "Ananya Verma"},
  {$addToSet: {courses: "AI Fundamentals"}}
)

--7. Update the city of a specific student to "Mumbai"
db.enrollments.updateOne(
  {name: "Sneha Kapoor"},
  {$set:{ "address.city": "Mumbai", "address.state": "Maharashtra" }}
)

--8.  Set feesPaid to true for all students from "Delhi"
db.enrollments.updateMany(
  { "address.city": "Delhi" },
  { $set: { feesPaid: true } }
)

--9. Remove "Java" course from any student who has it
db.enrollments.updateMany(
  {courses: "Java"},
  {$pull: {courses: "Java"}}
)

--10. Delete all students who have no courses enrolled (i.e., courses: [])
db.enrollments.deleteMany(
  {courses: {$size: 0}}
)
