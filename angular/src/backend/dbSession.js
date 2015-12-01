 var DBWrapper = require('node-dbi').DBWrapper; 
 var dbWrapper = new DBWrapper('sqlite3', {'path': '../../../db.sqlite3'});
 dbWrapper.connect();
 module.exports = dbWrapper;

