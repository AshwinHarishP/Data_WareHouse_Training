-- Section 1: Basic Document Modeling & Insertion

-- 1. Create a database called taskmanager
use taskmanager

-- 2. Insert 3 users into a users collection. Each should have:
db.users.insertMany([
  {
		name: "Rahul",
		email: "rahul@gmail.com",
		role: "admin",
		active: true
	},
  {
		name: "Ram",
		email: "ram@gmail.com",
		role: "manager",
		active: true
	},
  {
		name: "Kishore",
		email: "kishore@gmail.com",
		role: "developer",
		active: true
	}
])

-- 3. Insert 2 projects into a projects collection
db.project.insertMany([
  {
    title: "E-Commerce Application",
    description: "E-Commerce Application for the company ABC",
    startDate: new Date("2024-05-01"),
    status: "completed",
    createdBy: {
      _id: ObjectId("6831b14eb2785ec470715986"),
      name: "Ram"
    }
  },
  {
    title: "Car Booking Application",
    description: "Car Booking Application for the company XYZ",
    startDate: new Date("2025-02-01"),
    status: "active",
    createdBy: {
      _id: ObjectId("6831b14eb2785ec470715987"),
      name: "Kishore"
    }
  }
]);

-- 4. Insert 5 tasks into a tasks collection
const user1 = db.users.findOne({name: "Rahul"});
const user2 = db.users.findOne({name: "Ram"});
const user3 = db.users.findOne({name: "Kishore"});
const project1 = db.project.findOne({title: "E-Commerce Application"});
const project2 = db.project.findOne({title: "Car Booking Application"});
db.tasks.insertMany([
  {
    title: "User Authentication",
    assignedTo: user1._id,
    projectId: project1._id,
    priority: "high",
    dueDate: new Date("2025-05-25"),
    status: "active"
  },
  {
    title: "Storing sessions in H2 Database",
    assignedTo: user1._id,
    projectId:  project2._id,
    priority: "medium",
    dueDate: new Date("2025-05-20"),
    status: "completed"
  },
  {
    title: "Optimizing GPU",
    assignedTo: user2._id,
    projectId: project2._id,
    priority: "medium",
    dueDate: new Date("2024-02-02"),
    status: "active"
  },
  {
    title: "Finding nearby vehicles",
    assignedTo: user3._id,
    projectId: project1._id,
    priority: "high",
    dueDate: new Date("2025-01-01"),
    status: "active"
  },
  {
    title: "Navigation UI updation",
    assignedTo: user3._id,
    projectId: project1._id,
    priority: "low",
    dueDate: new Date("2025-10-10"),
    status: "active"
  }
]);


-- Section 2: Filtering & Querying

-- 5. Find all tasks with priority "high" that are not completed
db.tasks.find(
  {
		priority: "high",
		status: "active"
	}	
)

-- 6. Query all active users with role "developer"
db.users.find(
{
	role: "developer",
	active: true	
})

-- 7. Find all tasks assigned to a specific user (by ObjectId )
db.tasks.find({assignedTo: user3._id})

-- 8. Find all projects started in the last 30 days
const date = new Date();
date.setDate(date.getDate() - 30);
db.project.find({ startDate: { $gte: date } });


-- Section 3: Update Operations

-- 9. Change the status of one task to "completed"
db.tasks.updateOne(
  {title: "Navigation UI updation"},
  {$set: {status: "completed"}}
)

-- 10. Add a new role field called "teamLead" to one of the users
db.users.updateOne(
  { name: "Rahul" },
  { $set: { role: "teamLead" } }
)

-- 11. Add a new tag array to a task: ["urgent", "frontend"]
db.tasks.updateOne(
  {title: "Navigation UI updation"},
  {$set: {tag: ["urgent", "frontend"]}}
)


-- Section 4: Array and Subdocument Operations

-- 12. Add a new tag "UI" to the task’s tags array using $addToSet 
db.tasks.updateOne(
  {title: "Navigation UI updation"},
  {$addToSet: {tag: "UI"}}
)

-- 13. Remove "frontend" from a task’s tag list
db.tasks.updateOne(
    {title: "Navigation UI updation"},
  	{$pull: {tag: "frontend"}}
)

-- 14. Use $inc to increment a project ’s progress field by 10
db.project.updateOne(
  { title: "Car Booking Application" },
  { $inc: { progress: 10 } }
)

  
-- Section 5: Aggregation & Lookup

-- 15. Use $lookup to join tasks with users and show task title + assignee name
db.tasks.aggregate([
  {
    $lookup: {
      from: "users",               
      localField: "assignedTo",    
      foreignField: "_id",         
      as: "assignee"               
    }
  }
])

-- 16. Use $lookup to join tasks with projects , and filter tasks where project status = active
db.tasks.aggregate([
  {
    $lookup: {
      from: "project",
      localField: "projectId",
      foreignField: "_id",
      as: "projectDetails"
    }
  },
  {
    $unwind: "$projectDetails"
  },
  {
    $match: {
      "projectDetails.status": "active"
    }
  }
])

-- 17. Use $group to get count of tasks per status
db.tasks.aggregate([
  {
    $group: {
      _id: "$status",      
      count: { $sum: 1 }   
    }
  }
])

-- 18. Use $match , $sort , and $limit to get top 3 soonest due tasks
db.tasks.aggregate([
  {
    $match: {
      dueDate: { $exists: true }  
    }
  },
  {
    $sort: {
      dueDate: 1   
    }
  },
  {
    $limit: 3
  }
])





