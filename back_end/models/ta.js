const mongoose = require('mongoose')
const timestamp = require('mongoose-timestamp')

const TA_Schema = new mongoose.Schema({
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
    ta:{
        type: Boolean,
        required: true
    },
    password:{
        type: String,
        required: true, 
        trim: true
    }
})

TA_Schema.plugin(timestamp)

const TA = mongoose.model('TA', TA_Schema)
module.exports = TA