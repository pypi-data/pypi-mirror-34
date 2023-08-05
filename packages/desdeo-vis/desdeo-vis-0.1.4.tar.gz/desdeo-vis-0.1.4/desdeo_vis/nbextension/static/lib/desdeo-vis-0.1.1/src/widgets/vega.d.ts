/// <reference types="backbone" />
import { DOMWidgetModel, DOMWidgetView, ISerializers, WidgetModel } from '@jupyter-widgets/base';
import * as Backbone from 'backbone';
export declare class VegaModel extends DOMWidgetModel {
    defaults(): any;
    static serializers: ISerializers;
    static model_name: string;
    static model_module: string;
    static model_module_version: string;
    static view_name: string;
    static view_module: string;
    static view_module_version: string;
}
export declare class VegaView extends DOMWidgetView {
    spec: any;
    view: any;
    constructor(options?: Backbone.ViewOptions<WidgetModel> & {
        options?: any;
    });
    render(): void;
    mountView(): void;
    readonly vegaEl: any;
}
