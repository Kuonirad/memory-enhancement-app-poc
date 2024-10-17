const path = require('path');
const ESLintPlugin = require('eslint-webpack-plugin');

module.exports = {
  webpack: {
    alias: {
      // Add any custom aliases here if needed
    },
    plugins: [
      new ESLintPlugin({
        extensions: ['js', 'jsx'],
        failOnError: false,
      }),
    ],
  },
};
