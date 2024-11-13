import { ModuleOptions } from "webpack";

export function getLoaders(): ModuleOptions {
  const tsLoader = {
    test: /\.tsx?$/,
    use: 'ts-loader',
    exclude: /node_modules/,
  };
  const cssLoader = {
    test: /\.css$/i,
    use: ["style-loader", "css-loader"],
  };
  const imgLoader = {
    test: /\.(png|jpg|jpeg|gif)$/i,
    type: 'asset/resource'
  };
  const svgLoader = {
    test: /\.svg$/i,
    issuer: /\.[jt]sx?$/,
    use: [
      { 
        loader: '@svgr/webpack',
        options: { 
          icon: true,
          svgoConfig: {
            plugins: [
              {
                name: "convertColors",
                params: {
                  currentColor: true
                  }
                }
            ]
          }
        }
      }
    ],
  };

  return {
    rules: [tsLoader, cssLoader, imgLoader, svgLoader],
  }
}