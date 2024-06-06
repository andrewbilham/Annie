import {
  Container,
  Flex,
  Heading,
  Skeleton,
  Table,
  TableContainer,
  Tbody,
  Td,
  Th,
  Thead,
  Tr,
} from "@chakra-ui/react"
import { useSuspenseQuery } from "@tanstack/react-query"
import { createFileRoute } from "@tanstack/react-router"

import { Suspense } from "react"
import { ErrorBoundary } from "react-error-boundary"
import { SourcesService } from "../../client"
import ActionsMenu from "../../components/Common/ActionsMenu"
import Navbar from "../../components/Common/Navbar"

export const Route = createFileRoute("/_layout/sources")({
  component: Sources,
})

function SourcesTableBody() {
  const { data: sources } = useSuspenseQuery({
    queryKey: ["sources"],
    queryFn: () => SourcesService.readSources({}),
  })

  return (
    <Tbody>
      {sources.data.map((source) => (
        <Tr key={source.id}>
          <Td>{source.id}</Td>
          <Td>{source.source_name}</Td>
          
          <Td>
            <ActionsMenu type={"Source"} value={source} />
          </Td>
        </Tr>
      ))}
    </Tbody>
  )
}
function SourcesTable() {
  return (
    <TableContainer>
      <Table size={{ base: "sm", md: "md" }}>
        <Thead>
          <Tr>
            <Th>ID</Th>
            <Th>Name</Th>
            <Th>Actions</Th>
          </Tr>
        </Thead>
        <ErrorBoundary
          fallbackRender={({ error }) => (
            <Tbody>
              <Tr>
                <Td colSpan={4}>Something went wrong: {error.message}</Td>
              </Tr>
            </Tbody>
          )}
        >
          <Suspense
            fallback={
              <Tbody>
                {new Array(5).fill(null).map((_, index) => (
                  <Tr key={index}>
                    {new Array(4).fill(null).map((_, index) => (
                      <Td key={index}>
                        <Flex>
                          <Skeleton height="20px" width="20px" />
                        </Flex>
                      </Td>
                    ))}
                  </Tr>
                ))}
              </Tbody>
            }
          >
            <SourcesTableBody />
          </Suspense>
        </ErrorBoundary>
      </Table>
    </TableContainer>
  )
}

function Sources() {
  return (
    <Container maxW="full">
      <Heading size="lg" textAlign={{ base: "center", md: "left" }} pt={12}>
        Sources Management
      </Heading>

      <Navbar type={"Sources"} />
      <SourcesTable />
    </Container>
  )
}
