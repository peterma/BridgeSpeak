import React from 'react';

export const BrowserRouter = ({ children }) => children;
export const MemoryRouter = ({ children }) => children;
export const Link = ({ children, to, ...props }) => <a href={to} {...props}>{children}</a>;
export const useNavigate = () => jest.fn();
export const useLocation = () => ({ pathname: '/' });
export const useSearchParams = () => [new URLSearchParams(), jest.fn()];
export const useParams = () => ({});
export const useRouteMatch = () => ({ path: '/', url: '/' });
export const Switch = ({ children }) => children;
export const Route = ({ children }) => children;
export const Redirect = ({ to }) => <div data-testid="redirect" data-to={to} />;
export const NavLink = ({ children, to, ...props }) => <a href={to} {...props}>{children}</a>;
