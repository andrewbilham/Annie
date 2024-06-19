import { Button, Flex, Icon, useDisclosure } from "@chakra-ui/react"
import { FaPlus } from "react-icons/fa"

import AddUser from "../Admin/AddUser"
import AddItem from "../Items/AddItem"
import AddSource from "../Sources/AddSource"
import AddClaim from "../Claims/AddClaim"
import AddReferral from "../Referrals/AddReferral"

interface NavbarProps {
  type: string
}

const Navbar = ({ type }: NavbarProps) => {
  const addUserModal = useDisclosure()
  const addItemModal = useDisclosure()
  const addSourceModal = useDisclosure()
  const addClaimModal = useDisclosure()
  const addReferralModal = useDisclosure()

  return (
    <>
      <Flex py={8} gap={4}>
        {/* TODO: Complete search functionality */}
        {/* <InputGroup w={{ base: '100%', md: 'auto' }}>
                    <InputLeftElement pointerEvents='none'>
                        <Icon as={FaSearch} color='ui.dim' />
                    </InputLeftElement>
                    <Input type='text' placeholder='Search' fontSize={{ base: 'sm', md: 'inherit' }} borderRadius='8px' />
                </InputGroup> */}
        <Button
          variant="primary"
          gap={1}
          fontSize={{ base: "sm", md: "inherit" }}
          onClick={type === "User" ? addUserModal.onOpen 
            : type === "Item" ? addItemModal.onOpen 
            : type === "Source" ? addSourceModal.onOpen 
            : type === "Referral" ? addReferralModal.onOpen 
            : addClaimModal.onOpen}
        >
          <Icon as={FaPlus} /> Add {type}
        </Button>
        <AddUser isOpen={addUserModal.isOpen} onClose={addUserModal.onClose} />
        <AddItem isOpen={addItemModal.isOpen} onClose={addItemModal.onClose} />
        <AddSource isOpen={addSourceModal.isOpen} onClose={addSourceModal.onClose} />
        <AddClaim isOpen={addClaimModal.isOpen} onClose={addClaimModal.onClose} />
        <AddReferral isOpen={addReferralModal.isOpen} onClose={addReferralModal.onClose} />
      </Flex>
    </>
  )
}

export default Navbar
