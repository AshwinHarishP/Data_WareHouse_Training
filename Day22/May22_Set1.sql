-- Section 1: Working with Schemas & Data Types

-- 1.	Create a database named trainingdb
use trainingdb

--2. create a collection employee
db.createCollection("employees")

-- 3. Inserting 4 records 
db.employees.insertMany([
  {
    name: "Ram",
    age: 30,
    isManager: true,
    skills: ["ML", "SpringBoot", "Hibernate", "REST API"],
    joiningDate: new Date("2025-01-01"),
    profile: {
      linkedin: "https://ram/profile/linkedin.com",
      portfolio: "https://tinyurl/ram.com"
    }
  },
  {
    name: "Anil",
    age: 22,
    isManager: false,
    skills: ["Data Science", "Servlets", "MS SQL", "Power BI"],
    joiningDate: new Date("2024-10-22"),
    profile: {
      linkedin: "https://anil/profile/linkedin.com",
      portfolio: "https://tinyurl/anil.com"
    }
  },
  {
    name: "Yeshnow",
    age: 26,
    isManager: false,
    skills: ["Python"],
    joiningDate: new Date("2024-03-21"),
    profile: {
      linkedin: "https://yeshnow/profile/linkedin.com",
      portfolio: "https://tinyurl/yeshnow.com"
    }
  },
  {
    name: "Ashwin Harish",
    age: 22,
    isManager: true,
    skills: ["Hibernate", "Spring boot", "Kafka", "MicroService"],
    joiningDate: new Date("2024-02-21"),
    profile: {
      linkedin: "https://ashwinharish/profile/linkedin.com",
      portfolio: "https://tinyurl/ashwinharish.com"
    }
  }
])

-- 4. Query all employees who: Have more than 2 skills and Joined after a specific date 
db.employees.find({
  skills: { $exists: true },
  $where: "this.skills.length > 2 && this.joiningDate > new Date('2024-10-01')"
})

-- 5. Add a new field rating (float) to one employee 
db.employees.updateOne(
  {name: "Anil"},
  {$set: {rating: 4.6}}
)

-- 6. Find all employees with rating field of type double
db.employees.find({rating: {$type: "double"}})

-- 7. Exclude the _id field in a query result and show only name and skills
db.employees.find({}, {_id: 0, name: 1, skills: 1})


-- Section 2: One-to-One (Embedded)

-- 1. Create a database schooldb
use schooldb

-- 2. In the students collection, insert 3 student documents with: Embedded guardian sub-document ( name , phone , relation ) 
db.students.insertMany([
  {
    name: "Ashwin Harish",
    rollNo: 201,
    class: "IV Year - CSE",
    section: "A",
    guardian: {
      name: "A PREM KUMAR",
      phone: 9994059349,
      relation: "Father"
    }
  },
  {
    name: "Aravind",
    rollNo: 202,
    class: "IV Year - CSE",
    section: "A",
    guardian: {
      name: "Latha",
      phone: 8754018099,
      relation: "Mother"
    }
  },
  {
    name: "Rahul",
    rollNo: 203,
    class: "IV Year - ECE",
    section: "B",
    guardian: {
      name: "Suresh",
      phone: 8272192123,
      relation: "Father"
    }
  },
  {
    name: "John",
    rollNo: 204,
    class: "III Year - AD",
    section: "B",
    guardian: {
      name: "Mariya",
      phone: 7876543218,
      relation: "Mother"
    }
  }
])

-- 3. Query students where the guardian is their "Mother" 
db.students.find({"guardian.relation": "Mother"})

--4. Update the guardian's phone number for a specific student
db.students.updateOne(
  { name: "John" },
  { $set: { "guardian.phone": 1234567890 } }
)


-- Section 3: One-to-Many (Embedded) 

-- 1. In the same schooldb , create a teachers collection
db.createCollection("teachers")

-- 2. Insert documents where each teacher has an embedded array of classes they teach (e.g., ["Math", "Physics"] ) 
db.teachers.insertMany([
  {
    name: "Nivetha",
    dept: "Computer Science",
    courses: ["Python", "Java"]
  },
  {
    name: "Saravanan",
    dept: "S&H",
    courses: ["Math", "Physics"]
  },
  {
    name: "Anil Kumar",
    dept: "S&H",
    courses: ["Physics", "Chemistry", "Biology"]
  },
  {
    name: "Singaram",
    dept: "ECE",
    courses: ["Embedded System", "Digital Signals"]
  }
])

-- 3. Query teachers who teach "Physics
db.teachers.find({courses: "Physics"})

-- 4. Add a new class "Robotics" to a specific teacher's classes array
db.teachers.updateOne(
  {name: "Singaram"},
  {$push: {courses: "Robotics"}}
)

-- 5. Remove "Math" from one teacher’s class list 
db.teachers.updateOne(
  {name: "Saravanan"},
  {$pull: {courses: "Math"}}
)


-- Section 4: One-to-Many (Referenced) 

-- 1. Create a database academia
use academia

-- 2. Insert documents into course
db.createCollection("courses")
db.courses.insertMany([
  {
    _id: ObjectId("60d5f49f5f1b2c6d7f1e4e92"),
    title: "Hibernate crash course",
    credits: 6
  },
  {
    _id: ObjectId("60d5f4a45f1b2c6d7f1e4e93"),
    title: "Python for Data Science",
    credits: 8
  },
  {
    _id: ObjectId("60d5f4ab5f1b2c6d7f1e4e94"),
    title: "Advance Java",
    credits: 8
  },
  {
    _id: ObjectId("650d9f7e1a2b3c4d5e6f7890"),
    title: "SQL for Data Engineering",
    credits: 8
  }
])

-- 3. Insert documents into students
db.createCollection("students")
db.students.insertMany([
  {
    name: "Ashwin Harish",
    enrolledCourse: ObjectId("650d9f7e1a2b3c4d5e6f7890")
  },
  {
    name: "Ram",
    enrolledCourse: ObjectId("60d5f4a45f1b2c6d7f1e4e93")
  }
])

-- 4. Query students who are enrolled in a specific course
db.students.find({ enrolledCourse: ObjectId("650d9f7e1a2b3c4d5e6f7890") })

-- 5. Query the course details separately using the referenced _id 
const courseId = ObjectId("650d9f7e1a2b3c4d5e6f7890");
db.courses.find({ _id: courseId });


-- Section 5: $lookup (Join in Aggregation)

-- 1. Use the academia database
use academia

-- 2. Use $lookup to join students with courses based on enrolledCourse
db.students.aggregate([
  {
    $lookup: {
      from: "courses",
      localField: "enrolledCourse",
      foreignField: "_id",
      as: "courseDetails"
    }
  }
])

-- 3. Show only student name , and course title in the output using $project 
db.students.aggregate([
  {
    $lookup: {
      from: "courses",
      localField: "enrolledCourse",
      foreignField: "_id",
      as: "courseDetails"
    }
  },
  {
    $project: {
      _id: 0,
      name: 1,
      courseTitle: { $arrayElemAt: ["$courseDetails.title", 0] }
    }
  }
])

-- 4. Add a $match after $lookup to get only students enrolled in "Machine Learning" course
db.students.aggregate([
  {
    $lookup: {
      from: "courses",
      localField: "enrolledCourse",
      foreignField: "_id",
      as: "courseDetails"
    }
  },
  {
    $match: {
      courseDetails: {
        $elemMatch: { title: "Machine Learning" }
      }
    }
  }
])






