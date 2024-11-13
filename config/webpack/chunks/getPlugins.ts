import HtmlWebpackPlugin from 'html-webpack-plugin';
import { WebpackPluginInstance } from "webpack";
import CopyWebpackPlugin from "copy-webpack-plugin";

export function getPlugins(htmlTemplate: string): WebpackPluginInstance[] {
  const htmlWebpack = new HtmlWebpackPlugin({
    title: "Hello, webpack!",
    template: htmlTemplate,
    filename: "index.html"
  });

  const copyPlugin =  new CopyWebpackPlugin({
    patterns: [
      {
        from: "assets/img",
        to: "assets/img"
      }
    ]
  });

  return [
    htmlWebpack,
    copyPlugin
  ]
}