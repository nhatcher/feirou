import {
  TextField as MuiTextField,
  TextFieldProps as MuiTextFieldProps,
  styled,
} from "@mui/material";

export const TextField = (props: MuiTextFieldProps) => {
  return (
    <StyledTextField
      variant="outlined"
      InputLabelProps={{
        shrink: true,
      }}
      {...props}
    ></StyledTextField>
  );
};

const StyledTextField = styled(MuiTextField)(() => ({
  border: "none",
  backgroundColor: "#FFF",
}));

export default TextField;
