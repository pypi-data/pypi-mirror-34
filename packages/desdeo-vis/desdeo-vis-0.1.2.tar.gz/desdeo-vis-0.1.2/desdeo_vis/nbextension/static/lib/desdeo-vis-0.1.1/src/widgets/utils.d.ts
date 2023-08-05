export declare class SliderConf {
    readonly x: number;
    readonly y: number;
    readonly height: number;
    readonly min: number;
    readonly max: number;
    readonly inverted: number;
    readonly initValue: number;
    constructor(x: number, y: number, height: number, min: number, max: number, inverted: number, initValue: number);
    readonly initMinValue: number;
    readonly ideal: number;
    readonly nadir: number;
}
export interface PrefLt {
    readonly kind: '<';
}
export interface PrefLte {
    readonly kind: '<=';
    readonly val: number;
}
export interface PrefEq {
    readonly kind: '=';
}
export interface PrefGte {
    readonly kind: '>=';
    readonly val: number;
}
export interface PrefNeq {
    readonly kind: '<>';
}
export declare const PREF_KINDS: string[];
export declare const MAX_PREF_KINDS: string[];
export declare type DimPref = PrefLt | PrefLte | PrefEq | PrefGte | PrefNeq;
export declare function numToPref(val: number, conf: SliderConf, snap?: boolean): DimPref;
export declare function kindToPref(kind: string, conf: SliderConf): DimPref;
export declare function prefToDispNum(pref: DimPref, conf: SliderConf): number | null;
export declare function prefToNum(pref: DimPref, conf: SliderConf): number;
export declare function zip(firstArr: any[], ...arrs: any[][]): IterableIterator<any[]>;
