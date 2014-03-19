(function() {
  var names = ['Adam', 'tgwizard', 'Batman'];
  var index = Math.floor(Math.random()*3);

  print("> hello there, " + names[index]);
})();

EDITOR="/usr/bin/vim";

prompt = function() {
  var dbname = 'nodb';
  if (typeof db != 'undefined') {
    dbname = db;

    // This is supposed to "catch errors on writes" and "reconnect you
    // automatically if the shell gets disconnected"
    try {
      db.runCommand({getLastError: 1});
    } catch (e) {
      print(e);
    }
  }

  function get_formatted_date() {
    function p(x) {
      return x < 10 ? "0" + x : x;
    }
    var date = new Date();
    var y = date.getFullYear();
    var m = date.getMonth();
    var d = date.getDate();
    var h = date.getHours();
    var mm = date.getMinutes();
    var s = date.getSeconds();
    return y + "-" + p(m) + "-" + p(d) + " " + p(h) + ":" + p(mm) + ":" + p(s);
  }

  return "[" + get_formatted_date() + "] (" + dbname + ")\n↳ $ "
}
