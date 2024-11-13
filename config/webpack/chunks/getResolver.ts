import path from "path";
import { ResolveOptions } from "webpack";

export function getResolver(rootDir: string): ResolveOptions {
  const aliases = {
    "@components": path.resolve(rootDir, "src/components"),
    "@assets": path.resolve(rootDir, "assets"),
    "@domain": path.resolve(rootDir, "src/domain"),
    "@utils": path.resolve(rootDir, "src/utils"),
    "@projconfig": path.resolve(rootDir, "config"),
  };

  return {
    extensions: [".tsx", ".ts", ".js"],
    alias: aliases
  }
}