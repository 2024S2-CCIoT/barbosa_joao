import { QueryClient, QueryClientProvider } from '@tanstack/react-query';

export function withQuery(Component: React.ComponentType) {
  const displayName = Component.displayName || 'Component';

  const ComponentWithQuery = (props?: any) => {
    return (
      <QueryClientProvider client={new QueryClient()}>
        <Component {...props} />
      </QueryClientProvider>
    );
  };

  ComponentWithQuery.displayName = `withQuery(${displayName})`;

  return ComponentWithQuery;
}