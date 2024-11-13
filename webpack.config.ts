import path from "path";
import { Configuration } from 'webpack';
import { getWebpackConfig } from "./config/webpack/getWebpackConfig";
import { Paths } from "./config/webpack/types/Paths";

export default function buildWebpack(settings, argv): Configuration {
  const paths: Paths = {
    entryFile: path.resolve(__dirname, "src", "index.tsx"),
    outputDir: path.resolve(__dirname, "dist"),
    htmlTemplate: path.resolve(__dirname, "src/template", "index.html"),
    rootDir: __dirname
  }

  return getWebpackConfig(settings, argv, paths);
};