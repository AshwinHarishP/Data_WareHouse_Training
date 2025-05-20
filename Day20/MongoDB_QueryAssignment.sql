-- 1. Creating a DB
use faculty

-- 2. Creating a Collection
db.createCollection("professors")

-- 3.Insert the following 3 professors:
db.professors.insertMany([
  {
   	name: "Prem Kumar",
   	subject: "Mathematics",
   	experience: 10,
	 	active: true
  },
  {
		name: "Anand", 
		subject: "Physics",
		experience: 5,
		active: false
},
  {
		name: "Ram Kumar",
    subject: "Chemistry",
    experience: 8,
		active: true
}
])

-- 4. Find all professors in the professors collection
db.professors.find()

-- 5. Find only the professors who are active
db.professors.find({active: true})

-- 6. Update the experience of the "Physics" professor to 6 years
db.professors.updateOne(
{subject: "Physics"},
{$set: {experience: 6}}
)

--7. Mark the "Physics" professor as active
db.professors.updateOne(
{subject: "Physics"},
{$set: {active: true}}
)

-- 8. Delete the professor who teaches "Chemistry
db.professors.deleteOne({subject: "Chemistry"})
