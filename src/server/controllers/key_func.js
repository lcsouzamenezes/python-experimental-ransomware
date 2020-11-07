const key = require("./../models/keysave");
const logger = require("./../config/logger")
module.exports = {

    saveKey: async function (key) {
        return new Promise(async function(resolve, reject) {
            const newKey = new key ({
                key: key
            })

            newKey.save(function(err, obj){
                if(err){
                    logger.error(err)
                    resolve(false)
                }
                else {
                    logger.debug(obj)
                    resolve(true)
                }
            })
        });
    }
}
