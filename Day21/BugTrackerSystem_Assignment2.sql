-- 1. Creating a Database
use bugtracker
/* Output 
switched to db bugtracker
*/

-- Creating a Collection
db.createCollection("bugs")
/* Output
  { ok: 1 }
*/

-- 2. Inserting 3 bugs
db.bugs.insertMany([
{
	title: "Bug in admin page",
  reportedBy: "Ashwin Harish",
	status: "open",
  priority: "high",
  createdAt: new Date("2025-05-21")
},
{
	title: "Rate Limiting Bug",
	reportedBy: "Aravind",
	status: "in process",
  priority: "medium",
  createdAt: new Date("2025-04-02")
},
{
	title: "Home page reloading",
	reportedBy: "Akhilesh",
  status: "open",
  priority: "low",
  createdAt: new Date("2025-01-01")
}
])
/* Output
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('682db4e113d7632f2adced38'),
    '1': ObjectId('682db4e113d7632f2adced39'),
    '2': ObjectId('682db4e113d7632f2adced3a')
  }
}
*/

-- 3. Query all bugs With status: "open" and priority: "high"
db.bugs.find({status: "open", priority: "high"})
/* Output   
{
  _id: ObjectId('682db4e113d7632f2adced38'),
  title: 'Bug in admin page',
  reportedBy: 'Ashwin Harish',
  status: 'open',
  priority: 'high',
  createdAt: 2025-05-21T00:00:00.000Z
}
*/

-- 4. Update the status of a specific bug to "closed"
db.bugs.updateOne(
  {title: "Bug in admin page"},
  {$set: {status: "closed"}}
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

-- Inserting a new bug, reported by "Test User
db.bugs.insertOne(
{
	title: "Bug in Stories Section",
  reportedBy: "Test User",
	status: "open",
  priority: "low",
  createdAt: new Date("2025-05-13")
})
/* Output
{
  acknowledged: true,
  insertedId: ObjectId('682db5f713d7632f2adced3b')
}
*/

-- 5. Delete the bug that was reported by "Test User"
db.bugs.deleteOne({reportedBy: "Test User"})
/*Output 
{
  acknowledged: true,
  deletedCount: 1
}
*/

