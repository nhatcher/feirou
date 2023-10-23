import {
    createContext,
    useContext,
    useState,
    useEffect,
    ReactNode,
} from "react";
import { useCookies } from "react-cookie";

export interface ContextProps {
    isAuthenticated: boolean;
    login: (username: string, password: string) => Promise<void>;
    logout: () => Promise<void>;
}

type ProviderProps = {
    children: ReactNode;
};

export const AuthContext = createContext<ContextProps | null>(null);

export const AuthProvider = ({ children }: ProviderProps) => {
    const [isAuthenticated, setIsAuthenticated] = useState(false);
    const [isLoading, setIsLoading] = useState(true);
    const [cookies] = useCookies(["csrftoken", "locale"]);

    const login = async (username: string, password: string) => {
        const response = await fetch("/api/login/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": cookies.csrftoken,
                "Accept-Language": cookies.locale,
            },
            credentials: "same-origin",
            body: JSON.stringify({
                username,
                password,
            }),
        });

        const data = await response.json();
        console.log("Login response:", response.status, data);

        // Cookies are set in the backend
        if (response.status === 200) {
            setIsAuthenticated(true);
        } else {
            throw new Error(data.detail);
        }
    };

    const logout = async () => {
        await fetch("/api/logout", {
            credentials: "same-origin",
        });
        // Cookies are removed from the backend
        setIsAuthenticated(false);
    };

    useEffect(() => {
        const getSession = async () => {
            try {
                const response = await fetch("/api/session/", {
                    credentials: "same-origin",
                });
                const data = await response.json();
                console.log("SESSION:", data);

                setIsAuthenticated(!!data.authenticated);
                setIsLoading(false);
            } catch (err) {
                console.log("Get session error:", err);
            }
        };
        getSession();
    }, [isAuthenticated]);

    return (
        <>
            {isLoading ? null : (
                <AuthContext.Provider value={{ isAuthenticated, login, logout }}>
                    {children}
                </AuthContext.Provider>)}
        </>
    );
};

// custom hook
export const useAuth = (): ContextProps => {
    const context = useContext(AuthContext);

    if (context === null) {
        throw Error("useAuth must be used within AuthProvider");
    }
    return context;
};
