console.log("DietEntry.ts is on");

export class DietEntry {
    entryitem: string;
    entrycalories: number;
    entrydate: Date;
    constructor(item: string, calories: number, date: Date) {
        this.entryitem = item;
        this.entrycalories = calories;
        this.entrydate = date;
    }

    public toString(): string{
        return  "Ate: " + this.entryitem.toString() + 
                " which had " + this.entrycalories.toString() + " calories on " +
                this.entrydate.toString();
    }
}