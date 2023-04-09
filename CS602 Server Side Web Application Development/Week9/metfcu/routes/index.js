// Route to the routes ... routingly... 
const router = require('express').Router();
router.use('/api', require('./api'));
module.exports = router;