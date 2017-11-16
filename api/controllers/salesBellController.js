'use strict';
var player = require('play-sound')({player: 'omxplayer'})
var path = require('path');
const files = require('../constants');

exports.play_sound = function(req, res) {
  let fileName;
  const MIN_VOLUME = 3000;
  const amount = req.body.text ? parseInt(req.body.text) : 1000;
  const percent = (amount / 2000) - 1; // close to $2000, higher volume
  let volume = MIN_VOLUME * percent;

  if (req.body.text && parseInt(req.body.text) >= 2000) {
    fileName = files.GONG;
    volume = 0;
  } else {
    const userName = req.body.user_name;
    fileName = userName ? files[userName.toUpperCase()] || files.DEFAULT : files.DEFAULT;
  }

  var appDir = path.dirname(require.main.filename);
  player.play(appDir + '/assets/' + fileName, {omxplayer: ['-o', 'local', '--vol', volume]}, function(err){
    if (err) throw err
  })

  res.json({
    response_type: "in_channel",
    text: "Ding Ding Ding!"
  });
};
