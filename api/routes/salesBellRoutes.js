'use strict';
module.exports = function(app) {
  var salesBell = require('../controllers/salesBellController');

  app.route('/salesBell')
    .post(salesBell.play_sound);

};