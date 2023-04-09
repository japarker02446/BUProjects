"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
console.log("app.ts is on");
var jquery_1 = __importDefault(require("jquery")); //
var DietEntry_1 = require("./DietEntry");
var DietEntryArray_1 = require("./DietEntryArray");
var DietMinder = /** @class */ (function () {
    function DietMinder() {
        var _this = this;
        this.CLICK = "click";
        this.myDietArray = new DietEntryArray_1.DietEntryArray;
        // Add a new entry
        jquery_1.default("#btnsubmit").on(this.CLICK, function (event) {
            var fooditem = jquery_1.default("#fooditem").val();
            var foodcalories = jquery_1.default("foodcalories").val();
            var dateVal = jquery_1.default("fooddate").val();
            var fooddate = new Date(dateVal);
            var nextEntry = new DietEntry_1.DietEntry(fooditem, foodcalories, fooddate);
            _this.myDietArray.submitEntry(nextEntry);
            console.log("you clicked submit");
            //refreshDisplay();
        });
        //Edit an Entry
        jquery_1.default("btnedit").on(this.CLICK, function (event) {
            console.log("you clicked edit");
            // Get the array index of the item.
            // Change the value.
            // Change the content displayed.
            // refreshDisplay();
        });
        // Delete an entry
        jquery_1.default("butndelete").on(this.CLICK, function (event) {
            console.log("you clicked delete");
            // Get the array index of the item.
            // Delete the element.
            // Remove the element displayed.
            // refreshDisplay();
        });
    }
    return DietMinder;
}());
