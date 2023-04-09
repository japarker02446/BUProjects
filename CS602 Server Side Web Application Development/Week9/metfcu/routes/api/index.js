// Initalize server routes.
const router = require('express').Router();

router.use('/metfcu', require('./metfcu'));
router.use('/new', require('./metcreate'));
router.use('/list', require('./metlist'));
router.use('/trans', require('./mettransaction'));
router.use('/details', require('./metdetails'));

module.exports = router;