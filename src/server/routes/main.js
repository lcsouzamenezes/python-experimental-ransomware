const keysaver = require("./../controllers/key_func");
const logger = require("./../config/logger");
module.exports = function(app) {
    app.get('/', function(req, res) {
        res.status(200).json({
            "message":"Server is Online"
        })
    });

    app.post('/savekey', function(req, res) {
        if(req.body.key !== undefined) {
            const resp = keysaver.saveKey(req.body.key)
            if(resp) {
                // means that it successfully saved
                res.status(200).json({
                    "message": "Saved the key"
                })
            }
            else {
                res.status(500).json({
                    "message":"Abort! Could not find key"
                })
            }
        }
        else {
            res.status(403).json({
                "message":"Did not send the key"
            })
        }
    });
}
