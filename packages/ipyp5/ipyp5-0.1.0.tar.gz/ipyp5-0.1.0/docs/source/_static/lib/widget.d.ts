import { DOMWidgetModel, DOMWidgetView, ISerializers } from '@jupyter-widgets/base';
import { Sketch } from './sketch';
export declare class SketchModel extends DOMWidgetModel {
    defaults(): any;
    static serializers: ISerializers;
    static model_name: string;
    static model_module: string;
    static model_module_version: string;
    static view_name: string;
    static view_module: string;
    static view_module_version: string;
}
export declare class SketchView extends DOMWidgetView {
    sketch: Sketch;
    render(): void;
    remove(): void;
}
