import { createTheme } from '@mui/material'

export const lightTheme = createTheme({
  palette: {
    primary: {
      main: '#013A40'
    },
    secondary: {
      main: '#1E90FF'
    }
  },
  typography: {
    fontFamily: 'Roboto'
  },
  shape: {
    borderRadius: 0
  },
});


export const darkTheme = createTheme({
  palette: {
    primary: {
      main: '#013A40'
    },
    secondary: {
      main: '#1E90FF'
    }
  },
  typography: {
    fontFamily: 'Roboto'
  },
  shape: {
    borderRadius: 0
  },
});