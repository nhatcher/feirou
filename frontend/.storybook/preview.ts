import type { Preview } from "@storybook/react";
import { CssBaseline, ThemeProvider } from "@mui/material";
import { lightTheme, darkTheme } from "../src/Theme.js";

import { withThemeFromJSXProvider } from '@storybook/addon-themes';

import '@fontsource/roboto/300.css';
import '@fontsource/roboto/400.css';
import '@fontsource/roboto/500.css';
import '@fontsource/roboto/700.css';

const preview: Preview = {
  parameters: {
    actions: { argTypesRegex: "^on[A-Z].*" },
    controls: {
      matchers: {
        color: /(background|color)$/i,
        date: /Date$/,
      },
    },
  },
};


export const decorators = [withThemeFromJSXProvider({
  GlobalStyles: CssBaseline,
  Provider: ThemeProvider,
  themes: {
    light: lightTheme,
    dark: darkTheme,
  },
  defaultTheme: 'light',
})];

export default preview;
