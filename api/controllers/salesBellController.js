'use strict';
var player = require('play-sound')({player: 'omxplayer'})
var path = require('path');
const files = require('../constants');

exports.play_sound = function(req, res) {
  let fileName;
  console.log(req.body.text);
  console.log(parseInt(req.body.text));
  console.log(parseInt(req.body.text) >= 2000);

  if (req.body.text && parseInt(req.body.text) >= 2000) {
    fileName = files.GONG;
  } else {
    const userName = req.body.user_name;
    fileName = userName ? files[userName.toUpperCase()] || files.DEFAULT : files.DEFAULT;
  }

  var appDir = path.dirname(require.main.filename);
  player.play(appDir + '/assets/' + fileName, {omxplayer: ['-o', 'local']}, function(err){
    if (err) throw err
  })

  res.json("Ding Ding Ding!");
};
