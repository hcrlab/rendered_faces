var express = require('express');
var router = express.Router();
var mongo = require('mongodb').MongoClient;
var objectId = require('mongodb').ObjectID;
var assert = require('assert');

var url = 'mongodb://localhost:27017/testdb';

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index');
});

router.get('/get-data', function(req, res, next) {
  var resultArray = [];
  mongo.connect(url, function(err, db) {
    assert.equal(null, err);
    var cursor = db.collection('Data').find();
    cursor.forEach(function(doc, err) {
      assert.equal(null, err);
      resultArray.push(doc);
    }, function() {
      db.close();
      res.render('getdata.hbs', {items: resultArray});
    });
  });
});

router.post('/insert', function(req, res, next) {
  var item = {
    Name: req.body.Name,
    robottype: req.body.robottype,
    category: req.body.category
  };

  mongo.connect(url, function(err, db) {
    assert.equal(null, err);
    db.collection('Data').insertOne(item, function(err, result) {
      assert.equal(null, err);
      console.log('Item inserted');
      db.close();
    });
  });

  res.redirect('/');
});

router.search('/search', function(req, res, next) {

});

module.exports = router;
