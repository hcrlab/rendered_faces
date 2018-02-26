var async = require('async');
var Robot = require('../models/Robot');

/**
 * GET /
 */

exports.homeGet = function(req, res) {

    // query Mongoose to get list of all the robot names in the database
    Robot.find({}, {name:1, _id:0}, function(err, robots) {

        res.render('home', {
            title: 'Robot Facebook',
            robot_names: robots
        });
    });
};

/**
 * POST /
 */

exports.homePost = function(req, res) {

    console.log(req);

        res.render('home', {
            title: 'Robot Facebook'
        });
};