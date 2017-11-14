'use strict';
var player = require('play-sound')()
var path = require('path');
const files = require('../constants');

exports.play_sound = function(req, res) {
  console.log(req);
  var appDir = path.dirname(require.main.filename);
  player.play(appDir + '/assets/' + files.COLIN, function(err){
    if (err) throw err
  })

  res.json({message: "cool beans yo"});
};
