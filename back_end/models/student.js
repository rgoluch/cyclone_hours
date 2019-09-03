const mongoose = require('mongoose')
const timestamp = require('mongoose-timestamp')

const StudentSchema = new mongoose.Schema({
    name:{
        type: String,
        required: true,
        trim: true
    },
    net_id:{
        type: String,
        required: true, 
        trim: true
    },
    class:{
        type: String,
        required: true, 
        trim: true
    },
    password:{
        type: String,
        required: true, 
        trim: true
    }
})

StudentSchema.plugin(timestamp)

const Student = mongoose.model('Student', StudentSchema)
module.exports = Student