const express = require('express');
const bodyParser = require("body-parser");
const cors = require("cors");
const logger = require('./config/logger')
const morgan = require('morgan')
const rfs = require('rotating-file-stream') // version 2.x
const path = require('path')

const app = express();
app.use(bodyParser.urlencoded({extended: true}));
app.use(cors());

var accessLogStream = rfs.createStream('access.log', {
    interval: '1d', // rotate daily
    path: path.join(__dirname, 'log')
})

// setup the logger
app.use(morgan('combined', { stream: accessLogStream }))

require("./routes")(app);

app.listen(3000, "0.0.0.0", function (req,res) {
    logger.info("Server Started");
});
