'use strict';
var player = require('play-sound')({player: omxplayer})
var path = require('path');
const files = require('../constants');

exports.play_sound = function(req, res) {
  const userName = req.body.user_name;
  const fileName = userName ? files[userName.toUpperCase()] || files.DEFAULT : files.DEFAULT;

  var appDir = path.dirname(require.main.filename);
  player.play(appDir + '/assets/' + fileName, function(err){
    if (err) throw err
  })

  res.json("Ding Ding Ding!");
};
