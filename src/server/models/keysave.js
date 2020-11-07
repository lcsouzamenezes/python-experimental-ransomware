const mongoose = require("mongoose"); 

const keySchema = new mongoose.Schema({
    stamper: {type: Date, default:Date.now},
    key: {type: String, default:"Error"}
})

module.exports = mongoose.model("key", keySchema)

