import {
  Button,
  FormControl,
  FormErrorMessage,
  FormLabel,
  Input,
  Modal,
  ModalBody,
  ModalCloseButton,
  ModalContent,
  ModalFooter,
  ModalHeader,
  ModalOverlay,
} from "@chakra-ui/react"
import { useMutation, useQueryClient } from "@tanstack/react-query"
import { type SubmitHandler, useForm } from "react-hook-form"

import { type ApiError, type SourceCreate, SourcesService } from "../../client"
import useCustomToast from "../../hooks/useCustomToast"

interface AddSourceProps {
  isOpen: boolean
  onClose: () => void
}

const AddSource = ({ isOpen, onClose }: AddSourceProps) => {
  const queryClient = useQueryClient()
  const showToast = useCustomToast()
  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isSubmitting },
  } = useForm<SourceCreate>({
    mode: "onBlur",
    criteriaMode: "all",
    defaultValues: {
      source_name: "",
      //description: "",
    },
  })

  const mutation = useMutation({
    mutationFn: (data: SourceCreate) =>
      SourcesService.createSource({ requestBody: data }),
    onSuccess: () => {
      showToast("Success!", "Source created successfully.", "success")
      reset()
      onClose()
    },
    onError: (err: ApiError) => {
      const errDetail = (err.body as any)?.detail
      showToast("Something went wrong.", `${errDetail}`, "error")
    },
    onSettled: () => {
      queryClient.invalidateQueries({ queryKey: ["sources"] })
    },
  })

  const onSubmit: SubmitHandler<SourceCreate> = (data) => {
    mutation.mutate(data)
  }

  return (
    <>
      <Modal
        isOpen={isOpen}
        onClose={onClose}
        size={{ base: "sm", md: "md" }}
        isCentered
      >
        <ModalOverlay />
        <ModalContent as="form" onSubmit={handleSubmit(onSubmit)}>
          <ModalHeader>Add Source</ModalHeader>
          <ModalCloseButton />
          <ModalBody pb={6}>
            <FormControl isRequired isInvalid={!!errors.source_name}>
              <FormLabel htmlFor="source_name">Name</FormLabel>
              <Input
                id="source_name"
                {...register("source_name", {
                  required: "Name is required.",
                })}
                placeholder="Name"
                type="text"
              />
              {errors.source_name && (
                <FormErrorMessage>{errors.source_name.message}</FormErrorMessage>
              )}
            </FormControl>
            {/* <FormControl mt={4}>
              <FormLabel htmlFor="description">Description</FormLabel>
              <Input
                id="description"
                {...register("description")}
                placeholder="Description"
                type="text"
              />
            </FormControl> */}
          </ModalBody>

          <ModalFooter gap={3}>
            <Button variant="primary" type="submit" isLoading={isSubmitting}>
              Save
            </Button>
            <Button onClick={onClose}>Cancel</Button>
          </ModalFooter>
        </ModalContent>
      </Modal>
    </>
  )
}

export default AddSource
