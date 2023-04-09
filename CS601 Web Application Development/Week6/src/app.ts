console.log("app.ts is on");

import $ from 'jquery';//
import { DietEntry } from './DietEntry';
import { DietEntryArray } from './DietEntryArray';

class DietMinder {

    private CLICK:any = "click";
    [x: string]: any;
    private myDietArray = new DietEntryArray;

    constructor(){

        // Add a new entry
        $("#btnsubmit").on(this.CLICK, (event: MouseEvent) => {
            const fooditem:string = $("#fooditem").val() as string;
            const foodcalories:number = $("foodcalories").val() as number;
            const dateVal:string = $("fooddate").val() as string;
            const fooddate:Date = new Date(dateVal);

            var nextEntry = new DietEntry(fooditem, foodcalories, fooddate);
            this.myDietArray.submitEntry(nextEntry);
            console.log("you clicked submit");
            //refreshDisplay();
        });

        //Edit an Entry
        $("btnedit").on(this.CLICK, (event: MouseEvent) => {
            console.log("you clicked edit");
            // Get the array index of the item.
            // Change the value.
            // Change the content displayed.
           // refreshDisplay();
        });

        // Delete an entry
        $("butndelete").on(this.CLICK, (event: MouseEvent) => {
            console.log("you clicked delete");
            // Get the array index of the item.
            // Delete the element.
            // Remove the element displayed.
           // refreshDisplay();
        });
    }
}


