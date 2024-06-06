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

import {
  type ApiError,
  type SourcePublic,
  type SourceUpdate,
  SourcesService,
} from "../../client"
import useCustomToast from "../../hooks/useCustomToast"

interface EditSourceProps {
  source: SourcePublic
  isOpen: boolean
  onClose: () => void
}

const EditSource = ({ source, isOpen, onClose }: EditSourceProps) => {
  const queryClient = useQueryClient()
  const showToast = useCustomToast()
  const {
    register,
    handleSubmit,
    reset,
    formState: { isSubmitting, errors, isDirty },
  } = useForm<SourceUpdate>({
    mode: "onBlur",
    criteriaMode: "all",
    defaultValues: source,
  })

  const mutation = useMutation({
    mutationFn: (data: SourceUpdate) =>
      SourcesService.updateSource({ id: source.id, requestBody: data }),
    onSuccess: () => {
      showToast("Success!", "Source updated successfully.", "success")
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

  const onSubmit: SubmitHandler<SourceUpdate> = async (data) => {
    mutation.mutate(data)
  }

  const onCancel = () => {
    reset()
    onClose()
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
          <ModalHeader>Edit Source</ModalHeader>
          <ModalCloseButton />
          <ModalBody pb={6}>
            <FormControl isInvalid={!!errors.source_name}>
              <FormLabel htmlFor="source_name">Name</FormLabel>
              <Input
                id="source_name"
                {...register("source_name", {
                  required: "Name is required",
                })}
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
            <Button
              variant="primary"
              type="submit"
              isLoading={isSubmitting}
              isDisabled={!isDirty}
            >
              Save
            </Button>
            <Button onClick={onCancel}>Cancel</Button>
          </ModalFooter>
        </ModalContent>
      </Modal>
    </>
  )
}

export default EditSource
