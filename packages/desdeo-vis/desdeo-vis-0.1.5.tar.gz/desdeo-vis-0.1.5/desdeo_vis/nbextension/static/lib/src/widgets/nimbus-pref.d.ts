import { VegaModel, VegaView } from './vega';
import NimbusPref from './NimbusPref.vue';
export declare class NimbusPrefModel extends VegaModel {
    static model_name: string;
    static view_name: string;
}
export declare class NimbusPrefView extends VegaView {
    component: NimbusPref;
    vegaElement: HTMLDivElement;
    render(): void;
    onPrefsChange(newPrefProb: any, oldPrefProb: any): void;
    onMaxAsMinChange(newMaxAsMin: any, oldMaxAsMin: any): void;
    readonly vegaEl: HTMLDivElement;
}
