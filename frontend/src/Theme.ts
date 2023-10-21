import { createTheme } from '@mui/material'

export const theme = createTheme({
  palette: {
    primary: {
      main: '#800080'
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
  components: {
    MuiButton: {
        defaultProps: {
            variant: 'contained',
            disableRipple: true,
            color: 'primary'
        }
    },
    MuiTextField: {
        defaultProps: {
            variant: 'outlined',
            InputLabelProps: {
                shrink: true
            }
        }
    },
    MuiPaper: {
        defaultProps: {
            elevation: 0,
        }
    }
  }
});