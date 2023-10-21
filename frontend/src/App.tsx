import {
  Grid,
  TextField,
  Paper,
  Button,
  Divider,
  Link
} from '@mui/material';
import './App.css'

function App() {
  return (
    <div style={{ padding: 30 }}>
      <Paper>
        <Grid
          container
          spacing={3}
          direction={'column'}
          alignItems={'center'}
        >
          <Grid item xs={12}>
            <TextField label="Username"></TextField>
          </Grid>
          <Grid item xs={12}>
            <TextField label="Password" type={'password'}></TextField>
          </Grid>
          <Grid item xs={12}>
            <Link>Forgot password?</Link>
          </Grid>
          <Grid item xs={12}>
            <Button fullWidth>Sign In</Button>
            <Divider>or</Divider>
            <Button fullWidth>Create an account</Button>
          </Grid>
        </Grid>
      </Paper>
    </div>
  );
}

export default App
