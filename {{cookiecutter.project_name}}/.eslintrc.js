module.exports = {
  env: {
    browser: true,
    es2021: true,
  },
  extends: ["plugin:react/recommended", "airbnb", "prettier"],
  parserOptions: {
    ecmaFeatures: {
      jsx: true,
    },
    ecmaVersion: "latest",
    sourceType: "module",
  },
  plugins: ["react"],
  rules: {
    "react/jsx-filename-extension": [1, { extensions: [".tsx", ".ts"] }],
  },
  overrides: [
    {
      files: ["*.jsx"],
      rules: {
        "react/prop-types": "off",
      },
    },
  ],
};
