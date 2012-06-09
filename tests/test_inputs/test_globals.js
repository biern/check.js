// assign
defined1 = 1;

// member assign
depend2.asdf = 2;

// calls
depend3();

depend4.member();

depend5(depend7.m.n, depend8);

// vars
var notg = 2,
    notg10;

notg = 3;

depend1.on.me = 2;

notg.member = 4;
// function definitions
function defined5 (notg1, notg2, notg3) {
    function nested (notg4) {
        notg1 = 1;
        notg4 = 2;
        defined2 = 3;
    }

    function (local) {
        local = 2;
    }();

    notg1 = 2;
    notg2.member = 3;
    notg3();
    defined3 = 7;
}

function (local) {
    local = 2;
}();

defined4 = 6;

var x = depend2.on.me;

var y = 3 + depend6;