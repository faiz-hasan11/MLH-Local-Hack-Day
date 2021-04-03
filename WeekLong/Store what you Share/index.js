const dotenv = require('dotenv')
dotenv.config()
const mongodb = require('mongodb')


    mongodb.connect(process.env.CONNECTIONSTRING , {useUnifiedTopology: true} ,async function(err,client) {
        const db = client.db()
    //To Read
    // const results = await db.collection("Pets").find().toArray()

    // To Create
    // await db.collection("Pets").insertOne({name:"Bob",age:2})
    // console.log("ADDED")
    // const results = await db.collection("Pets").find().toArray()
    // console.log(results)

    //To Update
    // await db.collection("Pets").updateOne({_id:mongodb.ObjectID("60278ac450a9a4c400f989f7")} , {$set: {name:"john"} } )
    // console.log("Updated")
    // const results = await db.collection("Pets").find().toArray()
    // console.log(results)

    //To Delete
    await db.collection("Pets").deleteOne({_id:mongodb.ObjectID("60278ac450a9a4c400f989f7")})
    console.log("deleted")
    const results = await db.collection("Pets").find().toArray()
    console.log(results)

    client.close()
})

