"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var DietEntry = /** @class */ (function () {
    function DietEntry(item, calories, date) {
        this.entryitem = item;
        this.entrycalories = calories;
        this.entrydate = date;
    }
    DietEntry.prototype.toString = function () {
        return "Ate: " + this.entryitem.toString() +
            " which had " + this.entrycalories.toString() + " calories on " +
            this.entrydate.toString();
    };
    return DietEntry;
}());
exports.DietEntry = DietEntry;
