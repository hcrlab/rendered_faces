var express = require('express');
var router = express.Router();
var mongo = require('mongodb').MongoClient;
var objectId = require('mongodb').ObjectID;
var assert = require('assert');

var url = 'mongodb://localhost:27017/db';

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
    category: req.body.category,
      fullhead: req.body.fullhead,
      screentype: req.body.screentype,
      mouth: req.body.mouth,
      nose: req.body.nose,
      eyebrows: req.body.eyebrows,
      cheeksblush: req.body.cheeksblush,
      hair: req.body.hair,
      ears: req.body.ears,
      physicalfeatures: req.body.physicalfeatures,
      robotheight: req.body.robotheight,
      embodiment: req.body.embodiment,
      facecolor: req.body.facecolor,
      faceturnsothercolors: req.body.faceturnsothercolors,
      facegradientto: req.body.facegradientto,
      faceshape: req.body.faceshape,
      screensize: req.body.screensize,
      headmotion: req.body.headmotion,
      facemotion: req.body.facemotion,
      infodisplay: req.body.infodisplay,
      eyecolor: req.body.eyecolor,
      eyeoutlinecolor: req.body.eyeoutlinecolor,
      eyeturnsothercolorsinside: req.body.eyeturnsothercolorsinside,
      eyeshape: req.body.eyeshape,
      eyeturnsothershapesexcludeblink: req.body.eyeturnsothershapesexcludeblink,
      pupilyorn: req.body.pupilyorn,
      pupilcolor: req.body.pupilcolor,
      lid: req.body.lid,
      iris: req.body.iris,
      lashescolor: req.body.lashescolor,
      lashshape: req.body.lashshape,
      reflectedglarecolor: req.body.reflectedglarecolor,
      numberglarecircles: req.body.numberglarecircles,
      blinktype: req.body.blinktype,
      pupilshapes: req.body.pupilshapes,
      eyemotion: req.body.eyemotion,
      pupilandorirismotion: req.body.pupilandorirismotion,
      glaremotion: req.body.glaremotion,
      wink: req.body.wink,
      eyesize: req.body.eyesize,
      eyeplacement: req.body.eyeplacement,
      eyespacing: req.body.eyespacing,
      mouthcolororoutlinecolor: req.body.mouthcolororoutlinecolor,
      mouthinsidecolor: req.body.mouthinsidecolor,
      mouthshape: req.body.mouthshape,
      lips: req.body.lips,
      tongue: req.body.tongue,
      teethshape: req.body.teethshape,
      mouthmotion: req.body.mouthmotion,
      mouthlength: req.body.mouthlength,
      mouthplacement: req.body.mouthplacement,
      nosecolor: req.body.nosecolor,
      noseshape: req.body.noseshape,
      nose3d: req.body.nose3d,
      nosesize: req.body.nosesize,
      noseplacement: req.body.noseplacement,
      nosemotion: req.body.nosemotion,
      eyebrowcolor: req.body.eyebrowcolor,
      eyebrowshape: req.body.eyebrowshape,
      eyebrowinneredgepositions: req.body.eyebrowinneredgepositions,
      eyebrowindependentmotion: req.body.eyebrowindependentmotion,
      eyebrowmotion: req.body.eyebrowmotion,
      eyebrowlength: req.body.eyebrowlength,
      eyebrowarch: req.body.eyebrowarch,
      cheekcolor: req.body.cheekcolor,
      cheekshape: req.body.cheekshape,
      cheeksize: req.body.cheeksize,
      cheekplacement: req.body.cheekplacement,
      cheekspacing: req.body.cheekspacing,
      haircolor: req.body.haircolor,
      countryregionoforigin: req.body.countryregionoforigin,
      year: req.body.year

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

router.get('/display', function(req, res, next) {

  var resultArray = [];
  mongo.connect(url, function(err, db) {
    assert.equal(null, err);
    var cursor = db.collection('Data').find();
    cursor.forEach(function(doc, err) {
        assert.equal(null, err);
        resultArray.push(doc);
    }, function() {
      db.close();
      res.render('data.hbs', {items: resultArray});
      });

    });
});

module.exports = router;
