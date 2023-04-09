"use strict";
var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p]; };
        return extendStatics(d, b);
    }
    return function (d, b) {
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
Object.defineProperty(exports, "__esModule", { value: true });
console.log("DietEntryArray.ts is on");
var DietEntryArray = /** @class */ (function (_super) {
    __extends(DietEntryArray, _super);
    function DietEntryArray() {
        var _this = _super.call(this) || this;
        _this.dietEntries = [];
        return _this;
    }
    DietEntryArray.prototype.submitEntry = function (nextEntry) {
        this.dietEntries.push(nextEntry);
        console.log("you added an entry");
    };
    DietEntryArray.prototype.editEntry = function (editDex, newEntry) {
        this.dietEntries[editDex] = newEntry;
        console.log("you edited an entry");
    };
    DietEntryArray.prototype.deleteEntry = function (deleteDex) {
        this.dietEntries.splice(deleteDex, 1);
        console.log("you deleted an entry");
    };
    return DietEntryArray;
}(Array));
exports.DietEntryArray = DietEntryArray;
