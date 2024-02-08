import { ButtonProps as MuiButtonProps, Button as MuiButton, styled } from "@mui/material";

interface ButtonProps extends MuiButtonProps {
  /**
   * Is this the principal call to action on the page?
   */
  primary?: boolean;
}

/**
 * Primary UI component for user interaction
 */
export const Button = ({
  primary = false,
  fullWidth = false,
  children,
  ...props
}: ButtonProps) => {
  return (
    <StyledButton
      variant="contained"
      disableRipple={true}
      color="primary"
      {...props}
    >
      {children}
    </StyledButton>
  );
};

const StyledButton = styled(MuiButton)(() => ({
    borderRadius: "8px"
}));

export default Button;