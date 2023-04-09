console.log("DietEntryArray.ts is on");

import { DietEntry } from './DietEntry';

export class DietEntryArray extends Array {
    
    dietEntries:DietEntry[] = [];

    public constructor() {
        super();
    }

    public submitEntry(nextEntry: DietEntry): void{
        this.dietEntries.push(nextEntry);
        console.log("you added an entry");
    }

    public editEntry(editDex: number, newEntry: DietEntry): void {
        this.dietEntries[editDex] = newEntry;
        console.log("you edited an entry");
    }

    public deleteEntry(deleteDex: number): void{
        this.dietEntries.splice(deleteDex, 1);
        console.log("you deleted an entry");
    }
}